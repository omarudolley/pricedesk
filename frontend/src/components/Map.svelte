<script>
  import liberia from '$lib/data/liberia.topo.json'
  import * as Highcharts from 'highcharts'
  import { commodities, rates, websiteContent } from '$lib/data'
  import { currentLang, currentMapData, currentCurrency } from '$lib/stores'

  import HighchartsMapModule from 'highcharts/modules/map'

  import dataModule from 'highcharts/modules/data'
  import exportModule from 'highcharts/modules/exporting'
  import accessibilityModule from 'highcharts/modules/accessibility'
  import FaPlay from 'svelte-icons/fa/FaPlay.svelte'
  import FaPause from 'svelte-icons/fa/FaPause.svelte'
  import { onMount } from 'svelte'

  let mapChart
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

    dataModule(Highcharts)
    mapChart = Highcharts.mapChart({
      chart: {
        map: liberia,
        renderTo: 'container'
      },
      title: {
        text: websiteContent.select[$currentLang],
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
                return this.name + '<br>' + $currentCurrency.name + '$' + this.value
              }
            },
            style: {
              opacity: 0.95
            }
          },
          dataLabels: {
            enabled: true,
            allowOverlap: true,
            formatter: function () {
              if (this.point.value) {
                return `$${this.point.value}`
              } else {
                return 'no data'
              }
            },
            style: {
              fontSize: '10px'
            }
          }
        }
      ]
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
      mapChart.update({
        title: {
          text: websiteContent.select[$currentLang]
        }
      })
    }
  }

  $: $currentMapData, updateChart()
  $: $currentLang, updateChart()
</script>

<div class="map">
  <div id="container" />
  <div class="play-controls">
    <div class="play-pause-button" role="button" on:click={start}>
      {#if toPlay}
        <FaPlay />
      {:else}
        <FaPause />
      {/if}
    </div>
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
    margin: 2rem 0;
    box-shadow: 0px 0px 6px rgba(0, 0, 0, 0.45);
    border-radius: 0.5rem;
    padding: 0.5rem;

    @include mobile {
      margin-top: 1rem;
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
    display: flex;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
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
    padding: 5px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #0f62fe;

    svg {
      height: 1.2rem;
      width: 1.2rem;
    }
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
      color: black;
    }
  }
</style>
