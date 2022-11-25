<script>
  import StatusBar from '$components/StatusBar.svelte'
  import Map from '$components/Map.svelte'
  import ProductChart from '$components/ProductChart.svelte'
  import InflationChart from '$components/InflationChart.svelte'

  import { currentMapData } from '$lib/stores'

  function setModal(title) {
    modalItem = title
    open = true
  }

  let open = false
  let modalItem
</script>

<div class="container">
  <StatusBar {setModal} />
  {#if $currentMapData && modalItem}
    <ProductChart bind:data={$currentMapData} bind:open bind:modalItem />
  {/if}

  {#if $currentMapData}
    <Map bind:data={$currentMapData} />
  {/if}

  <InflationChart />
</div>

<style lang="scss">
  .container {
    @include mobile {
      padding: 1rem;
    }
  }
</style>
