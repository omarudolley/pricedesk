<script>
  import { currentListing, currentCurrency } from '$lib/stores'
  import { getTodayDate } from '$lib/utils'
  const today = getTodayDate()
</script>

<div class="container">
  <div class="inner">
    {#if $currentListing && typeof $currentListing !== 'undefined'}
      {#each Object.entries($currentListing?.[today] || {}) as [key, value]}
        <div class="item">
          <p class="name">{key}</p>
          <p class="value">{$currentCurrency.name} {value}</p>
        </div>
      {/each}
    {/if}
  </div>
</div>

<style lang="scss">
  .container {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 2rem;

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
  }
</style>
