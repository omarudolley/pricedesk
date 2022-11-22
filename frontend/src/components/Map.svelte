<script>
  import liberia from '$lib/data/liberia.topo.json'
  import * as Highcharts from 'highcharts'
  import { commodities, rates, locations, websiteContent } from '$lib/data'
  import { currentLang, currentMapData, currentCurrency } from '$lib/stores'

  import HighchartsMapModule from 'highcharts/modules/map'
  import drilldown from 'highcharts/modules/drilldown'
  import dataModule from 'highcharts/modules/data'
  import exportModule from 'highcharts/modules/exporting'
  import accessibilityModule from 'highcharts/modules/accessibility'
  import FaPlay from 'svelte-icons/fa/FaPlay.svelte'
  import FaPause from 'svelte-icons/fa/FaPause.svelte'
  import { onMount } from 'svelte'

  let mapChart
  let lineChart
  let toPlay = true
  let selected
  export let data
  export let value

  $: value = $currentMapData.dates.length - 1
  $: output = $currentMapData.dates[value]
  $: max = $currentMapData.dates.length - 1

  onMount(() => {
    HighchartsMapModule(Highcharts)
    exportModule(Highcharts)
    accessibilityModule(Highcharts)
    drilldown(Highcharts)
    dataModule(Highcharts)
    mapChart = Highcharts.mapChart({
      chart: {
        map: liberia,
        renderTo: 'container'
      },
      title: {
        text: 'Select item: ',
        fontSize: 10,
        x: 0,
        align: 'left',
        y: 20
      },

      mapNavigation: {
        enabled: true,
        buttonOptions: {
          verticalAlign: 'bottom'
        }
      },
      colorAxis: {
        minColor: '#FDFFDC',
        maxColor: '#B20213'
      },
      series: [
        {
          data: $currentMapData[selected.en][0].data.slice(),
          joinBy: null,
          name: selected.en,

          states: {
            hover: {
              brightness: 0.15
            }
          },
          tooltip: {
            pointFormat: '{point.name}<br> {point.value}<br>',

            backgroundColor: '#ffffff',
            pointFormatter: function () {
              if (this.value === undefined) {
                return 0
              } else {
                return $currentCurrency.name + ' $ ' + this.value
              }
            },
            style: {
              opacity: 0.95
            }
          },
          dataLabels: {
            enabled: true,
            allowOverlap: true,
            format: null,
            formatter: function () {
              if (this.point.value) {
                return `${this.point.name} <br> ${$currentCurrency.name} $ ${this.point.value}`
              } else {
                return this.point.name
              }
            },
            style: {
              fontWeight: '500',
              fontSize: '9px',
              color: '#000000',
              'text-anchor': 'middle',
              textOutline: '1px solid #ffffff80',
              textShadow: '0px 0px 2px #ffffff8c',
              textDecoration: 'none'
            }
          }
        }
      ]
    })

    lineChart = Highcharts.chart('line', {
      chart: {
        type: 'line'
      },
      title: {
        text: `${selected.en} over time `
      },
      xAxis: {
        categories: $currentMapData.dates
      },
      yAxis: {
        title: {
          text: `Price in ${$currentCurrency.name}`
        }
      },
      plotOptions: {
        line: {
          dataLabels: {
            enabled: true
          },
          enableMouseTracking: false
        }
      },
      series: generateLineChartSeries()
    })
  })

  function play() {
    if (value < max) {
      value++
    } else {
      value = 0
    }
    updateChart()

    if (value >= max) {
      toPlay = !toPlay
      clearTimeout(mapChart.sequenceTimer)
      mapChart.sequenceTimer = undefined
    }
  }

  function start() {
    toPlay = !toPlay

    if (mapChart.sequenceTimer === undefined) {
      mapChart.sequenceTimer = setInterval(function () {
        play()
      }, 500)
    } else {
      clearTimeout(mapChart.sequenceTimer)
      mapChart.sequenceTimer = undefined
    }
  }

  function onInput(evt) {
    value = evt.target.value
    updateChart()
  }

  function updateChart() {
    if (mapChart) {
      mapChart.series[0].setData(data[selected.en][value].data)
      mapChart.series[0].setName(selected[$currentLang])
    }
    if (lineChart) {
      lineChart.update({
        series: generateLineChartSeries(),
        yAxis: {
          title: {
            text: `${websiteContent.lineChartYaxis[$currentLang]} ${$currentCurrency.name}`
          }
        },
        title: {
          text: `${selected[$currentLang]} ${websiteContent.lineChartTitle[$currentLang]} `
        }
      })
    }
  }

  function generateLineChartSeries() {
    let items = $currentMapData[selected.en]
    let series = []
    locations.map((location) => {
      let obj = {
        name: '',
        data: []
      }
      obj.name = location
      items.map((item, index) => obj.data.push(items[index].data[locations.indexOf(location)]))
      series.push(obj)
    })
    return series
  }

  $: $currentMapData, updateChart()
  $: $currentLang, updateChart()
</script>

<div class="map">
  <div id="container" />
  <div class="play-controls">
    <button class="play-pause-button" on:click={start}>
      {#if toPlay}
        <FaPlay />
      {:else}
        <FaPause />
      {/if}
    </button>
    <input
      id="play-range"
      class="play-range"
      type="range"
      {value}
      min="0"
      {max}
      on:input={onInput}
      on:change={updateChart}
    />
    <output class="play-output" for="play-range" name="year">{output}</output>
  </div>
  <div class="select-box">
    <select class="select" bind:value={selected} on:change={updateChart}>
      {#each commodities as commodity}
        <option value={commodity}>{commodity[$currentLang]}</option>
      {/each}
      {#each rates as rate}
        <option value={rate}>{rate[$currentLang]}</option>
      {/each}
    </select>
  </div>

  <div id="line" />
</div>

<style global lang="scss">
  #container {
    height: 800px;
    min-width: 310px;
    max-width: 1200px;
    margin: 0 auto;

    @include mobile {
      max-height: 500px;
      max-width: 400px;
    }
  }

  .map {
    position: relative;
    margin-top: 5rem;
    @include mobile {
      margin-top: 3rem;
    }
  }

  .loading {
    margin-top: 10em;
    text-align: center;
    color: gray;
  }
  .play-controls {
    text-align: center;
    min-width: 310px;
    max-width: 800px;
    margin: 0 auto;
    padding: 5px 0 1em 0;
  }
  .play-controls * {
    display: inline-block;
    vertical-align: middle;
  }
  .play-pause-button {
    width: 30px;
    height: 30px;
    text-align: center;
    font-size: 15px;
    cursor: pointer;
    border: 1px solid silver;
    border-radius: 3px;
    background: #f8f8f8;
  }
  .play-range {
    margin: 2.5%;
    width: 70%;
  }

  .select-box {
    position: absolute;
    top: 0.75rem;
    left: 8rem;
    font-size: 1rem;

    @include mobile {
      left: 35%;
    }
    .select {
      position: -webkit-sticky;
      position: sticky;
      top: 0;
      padding: 5px;
    }
  }
</style>
