<script>
  import data from '$lib/data/inflation/data.json'
  import * as Highcharts from 'highcharts'
  import { websiteContent } from '$lib/data'
  import { currentLang } from '$lib/stores'

  import dataModule from 'highcharts/modules/data'
  import exportModule from 'highcharts/modules/exporting'
  import accessibilityModule from 'highcharts/modules/accessibility'
  import HighchartsMapModule from 'highcharts/modules/map'
  import { onMount } from 'svelte'
  let inflationChart

  onMount(() => {
    exportModule(Highcharts)
    accessibilityModule(Highcharts)
    dataModule(Highcharts)
    HighchartsMapModule(Highcharts)

    inflationChart = Highcharts.chart('inflation-line', {
      chart: {
        type: 'line'
      },
      title: {
        text: websiteContent.inflationRate[$currentLang]
      },
      xAxis: {
        categories: data.dates
      },
      yAxis: {
        title: {
          text: websiteContent.rate[$currentLang]
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
      series: [
        {
          name: 'Inflation',
          data: data.data
        }
      ]
    })
  })

  function update() {
    if (inflationChart) {
      inflationChart.update({
        yAxis: {
          title: {
            text: websiteContent.rate[$currentLang]
          }
        },
        title: {
          text: websiteContent.inflationRate[$currentLang]
        }
      })
    }
  }

  $: $currentLang, update()
</script>

<div class="inflation-line" id="inflation-line" />

<style lang="scss">
  .inflation-line {
    margin-top: 2rem;
    border: 0.5px solid gray;
    padding: 0.5rem;
  }
</style>
