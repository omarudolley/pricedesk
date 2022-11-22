<script>
  import StatusBar from '$components/StatusBar.svelte'
  import Map from '$components/Map.svelte'
  import { currentMapData } from '$lib/stores'
</script>

<div class="container">
  <StatusBar />

  {#if $currentMapData}
    <Map bind:data={$currentMapData} />
  {/if}
</div>

<style lang="scss">
  .container {
    @include mobile {
      padding: 1rem;
    }
  }
</style>
