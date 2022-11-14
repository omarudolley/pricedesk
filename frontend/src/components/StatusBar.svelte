<script>
  import { currentListing } from '$lib/stores'
  import RenderStatusItem from '$components/RenderStatusItem.svelte'
  import { commodities } from '$lib/data'
</script>

<div class="inner">
  {#if $currentListing && typeof $currentListing !== 'undefined'}
    {@const priceListing = Object.freeze($currentListing)}
    {#each commodities as title}
      <RenderStatusItem {title} {priceListing} />
    {/each}
  {/if}
</div>

<style lang="scss">
  .inner {
    display: grid;
    margin: 0 auto;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    justify-self: stretch;
    gap: 8px;
    justify-items: left;
    padding: 30px;
    background: rgba(255, 255, 255, 0.6);
    box-shadow: rgba(0, 0, 0, 0.1) 0px 0px 0px 0.5px inset;
    backdrop-filter: blur(40px);
    border-radius: 20px;
  }
</style>
