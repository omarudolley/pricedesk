<script>
  import { currentListing, currentLang } from '$lib/stores'
  import RenderStatusItem from '$components/RenderStatusItem.svelte'
  import { websiteContent, rates, commodityGrid } from '$lib/data'

  export let setModal
</script>

<div class="wrapper">
  {#if $currentListing && typeof $currentListing !== 'undefined'}
    {@const priceListing = Object.freeze($currentListing)}
    <div class="header-wrapper">
      <div class="header">{websiteContent.intro[$currentLang]}</div>
      {#each rates as title}
        <RenderStatusItem {title} {priceListing} {setModal} />
      {/each}
    </div>
    <div class="underline">
      <hr />
    </div>

    <div class="app">
      {#each Object.keys(commodityGrid).sort() as key}
        <h4 class="sub-header">{key}</h4>
        <div class="hs full" style="--total: {commodityGrid[key].length}">
          {#each commodityGrid[key].sort( (a, b) => a[$currentLang].localeCompare(b[$currentLang]) ) as title}
            <RenderStatusItem {title} {priceListing} {setModal} />
          {/each}
        </div>
      {/each}
    </div>
  {/if}
</div>

<style lang="scss">
  .wrapper {
    position: relative;
    background: $color-primary;
    margin-bottom: 2rem;
    padding: 0.5rem;

    .header-wrapper {
      display: grid;
      margin: 0 auto;
      grid-template-columns: repeat(auto-fit, minmax(13.75rem, 1fr));
      justify-self: stretch;
      gap: 1rem;
      justify-items: left;
      padding: 1.875rem;
      grid-auto-rows: 1fr;
      padding-bottom: 0.2rem;

      @include mobile {
        grid-auto-rows: auto;
      }
    }

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

    .underline {
      padding: 0 2rem;
    }
  }

  .app {
    --gutter: 1rem;

    display: grid;
    grid-gap: var(--gutter) 0;
    grid-template-columns: var(--gutter) 1fr var(--gutter);
    align-content: start;
    overflow-y: scroll;
    padding: 1.875rem;
  }

  .app > * {
    grid-column: 2 / -2;
  }

  .app > .full {
    grid-column: 1 / -1;
  }

  .hs {
    display: grid;
    gap: 1rem;
    grid-template-columns: repeat(var(--total), 14rem);

    overflow-x: scroll;
    scroll-snap-type: x proximity;
    padding: 1rem 0;
  }

  .sub-header {
    margin: 0;
    padding: 0;
    border-radius: 0.625rem;
    font-weight: 600;
    font-size: 1.5rem;
    @include mobile {
      font-size: 1rem;
    }
  }
</style>
