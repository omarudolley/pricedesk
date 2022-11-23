<script>
  import data from '$lib/data/inflation/data.json'
  import * as Highcharts from 'highcharts'

  import dataModule from 'highcharts/modules/data'
  import exportModule from 'highcharts/modules/exporting'
  import accessibilityModule from 'highcharts/modules/accessibility'
  import { onMount } from 'svelte'

  onMount(() => {
    exportModule(Highcharts)
    accessibilityModule(Highcharts)
    dataModule(Highcharts)

    Highcharts.chart('inflation-line', {
      chart: {
        type: 'line'
      },
      title: {
        text: 'Inflation rate'
      },
      xAxis: {
        categories: data.dates
      },
      yAxis: {
        title: {
          text: 'Rate'
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
</script>

<div class="inflation-line" id="inflation-line" />

<style lang="scss">
  .inflation-line {
    margin-top: 2rem;
  }
</style>
