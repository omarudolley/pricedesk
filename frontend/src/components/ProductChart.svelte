<script>
  import * as Highcharts from 'highcharts'
  import { locations, websiteContent } from '$lib/data'
  import { currentLang, currentMapData, currentCurrency } from '$lib/stores'

  import { Modal } from 'carbon-components-svelte'
  export let open = false

  import HighchartsMapModule from 'highcharts/modules/map'

  import dataModule from 'highcharts/modules/data'
  import exportModule from 'highcharts/modules/exporting'
  import accessibilityModule from 'highcharts/modules/accessibility'
  import { onMount } from 'svelte'

  let lineChart

  export let data
  export let value
  export let modalItem

  $: value = $currentMapData.dates.length - 1

  onMount(() => {
    HighchartsMapModule(Highcharts)
    exportModule(Highcharts)
    accessibilityModule(Highcharts)

    dataModule(Highcharts)

    lineChart = Highcharts.chart('line', {
      chart: {
        type: 'line'
      },
      title: {
        text: `${modalItem.en} over time `
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

  function updateChart() {
    if (lineChart) {
      lineChart.update({
        series: generateLineChartSeries(),
        yAxis: {
          title: {
            text: `${websiteContent.lineChartYaxis[$currentLang]} ${$currentCurrency.name}`
          }
        },
        title: {
          text: `${modalItem[$currentLang]} ${websiteContent.lineChartTitle[$currentLang]} `
        }
      })
    }
  }

  function generateLineChartSeries() {
    let items = $currentMapData[modalItem.en]
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
  $: modalItem, updateChart()
</script>

<Modal passiveModal bind:open on:open on:close>
  <div class="line">
    <div id="line" />
  </div>
</Modal>

<style>
  :global(.bx--modal-container) {
    box-shadow: 0px 0px 6px rgba(0, 0, 0, 0.45);
    border-radius: 0.5rem;
    background: white;
  }
  :global(.bx--modal-header__heading) {
    display: none;
  }
</style>
