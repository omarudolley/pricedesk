<script>
  import { currentListing } from '$lib/stores'
  import RenderStatus from '$components/RenderStatus.svelte'
  import { commodities } from '$lib/data'
</script>

<div class="inner">
  {#if $currentListing && typeof $currentListing !== 'undefined'}
    {@const priceListing = Object.freeze($currentListing)}
    {#each commodities as title}
      <RenderStatus {title} {priceListing} />
    {/each}
  {/if}
</div>

<style lang="scss">
  .inner {
    max-width: 80rem;
    margin: auto;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    width: 100%;
    grid-gap: 1.5rem;
  }
</style>
