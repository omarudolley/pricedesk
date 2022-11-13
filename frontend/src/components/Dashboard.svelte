<script>
  import { currentListing, currentCurrency } from '$lib/stores'
  import { getLastElement } from '$lib/utils'
</script>

<div class="inner">
  {#if $currentListing && typeof $currentListing !== 'undefined'}
    {@const priceListing = Object.entries(getLastElement($currentListing))}
    {#each priceListing as [key, value]}
      <div class="item">
        <p class="name">{key}</p>
        <p class="value">{$currentCurrency.name} {value}</p>
      </div>
    {/each}
  {/if}
</div>

<style lang="scss">
  .inner {
    max-width: 80rem;
    margin: auto;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    width: 100%;
    grid-gap: 2rem;

    .item {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    }
  }
</style>
