<script>
  import { currentListing } from '$lib/stores'
  import RenderStatusItem from '$components/RenderStatusItem.svelte'
  import { commodities } from '$lib/data'
</script>

<div class="wrapper">
  {#if $currentListing && typeof $currentListing !== 'undefined'}
    {@const priceListing = Object.freeze($currentListing)}
    <div class="inner top">
      <div class="header">Follow the Liberian market easily in one place.</div>
      <RenderStatusItem title="USD buying rate" {priceListing} />
      <RenderStatusItem title="USD selling rate" {priceListing} />
    </div>
    <div class="underline">
      <hr />
    </div>

    <div class="inner bottom">
      {#each commodities as title}
        <RenderStatusItem {title} {priceListing} />
      {/each}
    </div>
  {/if}
</div>

<style lang="scss">
  .wrapper {
    background: #8fc2ff;
    border-radius: 1.25rem;

    .header {
      width: 100%;

      padding: 0.625rem;
      border-radius: 0.625rem;
      grid-column: span 2;
      font-weight: 600;
      font-size: 1.5rem;
      @include mobile {
        font-size: 1rem;
        grid-column: span 1;
      }
    }
    .inner {
      display: grid;
      margin: 0 auto;
      grid-template-columns: repeat(auto-fit, minmax(13.75rem, 1fr));
      justify-self: stretch;
      gap: 0.5rem;
      justify-items: left;
      padding: 1.875rem;
      grid-auto-rows: 1fr;
    }
    .top {
      padding-bottom: 0.2rem;
    }

    .bottom {
      padding-top: 0.2rem;
    }
    .underline {
      padding: 0 2rem;
    }
  }
</style>
