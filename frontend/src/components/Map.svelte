<script>
  import liberia from '$lib/data/liberia.topo.json'
  import * as Highcharts from 'highcharts'
  import { commodities } from '$lib/data'
  import { currentLang, currentMapData } from '$lib/stores'

  import HighchartsMapModule from 'highcharts/modules/map'
  import drilldown from 'highcharts/modules/drilldown'
  import dataModule from 'highcharts/modules/data'
  import exportModule from 'highcharts/modules/exporting'
  import accessibilityModule from 'highcharts/modules/accessibility'
  import FaPlay from 'svelte-icons/fa/FaPlay.svelte'
  import FaPause from 'svelte-icons/fa/FaPause.svelte'
  import { onMount } from 'svelte'

  let chart
  let toPlay = true
  let selected
  export let data
  export let value

  $: value = $currentMapData.dates.length - 1
  $: output = $currentMapData.dates[value]
  $: max = $currentMapData.dates.length - 1

  $: {
    console.log(chart)
  }

  onMount(() => {
    HighchartsMapModule(Highcharts)
    exportModule(Highcharts)
    accessibilityModule(Highcharts)
    drilldown(Highcharts)
    dataModule(Highcharts)
    chart = Highcharts.mapChart({
      chart: {
        map: liberia,
        renderTo: 'container'
      },
      title: {
        text: selected,
        fontSize: 10,
        align: 'center',
        y: 15,
        style: {
          fontSize: 18
        }
      },
      mapNavigation: {
        enabled: true,
        buttonOptions: {
          verticalAlign: 'bottom'
        }
      },
      colorAxis: {
        min: 0,
        max: 24
      },
      series: [
        {
          data: $currentMapData[selected][0].data.slice(),
          joinBy: null,
          name: selected,

          states: {
            hover: {
              color: '#a4edba'
            }
          },
          tooltip: {
            pointFormat: '{point.name}<br> $ {point.value}<br>',

            backgroundColor: '#ffffff',
            style: {
              opacity: 0.95
            }
          },
          dataLabels: {
            enabled: true,
            allowOverlap: true,
            format: '{point.name}<br> $ {point.value}',
            style: {
              fontSize: '8px'
            }
          }
        }
      ]
    })
  })

  function update() {
    if (value < max) {
      value++
    } else {
      value = 0
    }
    updateChart()

    if (value >= max) {
      clearTimeout(chart.sequenceTimer)
      chart.sequenceTimer = undefined
    }
  }

  function start() {
    toPlay = !toPlay

    if (chart.sequenceTimer === undefined) {
      chart.sequenceTimer = setInterval(function () {
        update()
      }, 500)
    } else {
      clearTimeout(chart.sequenceTimer)
      chart.sequenceTimer = undefined
    }
  }
  function onChange() {
    updateChart()
  }
  function onInput(evt) {
    value = evt.target.value
    updateChart()
  }

  function updateChart() {
    if (chart) chart.series[0].setData(data[selected][value].data)
  }

  function onSelect() {
    chart.update({
      title: {
        text: selected
      },
      series: [{ name: selected }]
    })
    updateChart()
  }

  $: $currentMapData, updateChart()
</script>

<div class="map">
  <div id="container" />
  <div class="play-controls">
    <button class="play-pause-button" on:click={start} title="play">
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
      on:change={onChange}
    />
    <output class="play-output" for="play-range" name="year">{output}</output>
  </div>

  <select class="select" bind:value={selected} on:change={onSelect}>
    {#each commodities as commodity}
      <option value={commodity['en']}>{commodity[$currentLang]}</option>
    {/each}
  </select>
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
    border: 1px solid gray;
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

  .select {
    position: absolute;
    top: 0.75rem;
    left: 0.5rem;

    @include mobile {
      font-size: 0.5rem;
    }
  }
</style>
