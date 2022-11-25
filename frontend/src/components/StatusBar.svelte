<script>
  import { currentListing, currentLang } from '$lib/stores'
  import RenderStatusItem from '$components/RenderStatusItem.svelte'
  import { commodities, websiteContent, rates } from '$lib/data'

  export let setModal

  let sortedCommodities = commodities.sort((a, b) => a[$currentLang].localeCompare(b[$currentLang]))

  $: $currentLang,
    (sortedCommodities = sortedCommodities.sort((a, b) =>
      a[$currentLang].localeCompare(b[$currentLang])
    ))
</script>

<div class="wrapper">
  {#if $currentListing && typeof $currentListing !== 'undefined'}
    {@const priceListing = Object.freeze($currentListing)}
    <div class="inner top">
      <div class="header">{websiteContent.intro[$currentLang]}</div>
      {#each rates as title}
        <RenderStatusItem {title} {priceListing} {setModal} />
      {/each}
    </div>
    <div class="underline">
      <hr />
    </div>

    <div class="inner bottom">
      {#each sortedCommodities as title}
        <RenderStatusItem {title} {priceListing} {setModal} />
      {/each}
    </div>
  {/if}
</div>

<style lang="scss">
  .wrapper {
    position: relative;
    max-height: 39rem;
    overflow-y: scroll;
    background: #8fc2ff;
    margin-bottom: 2rem;
    box-shadow: 0px 0px 6px rgba(0, 0, 0, 0.45);
    border-radius: 0.5rem;
    padding: 0.5rem;

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
      gap: 1rem;
      justify-items: left;
      padding: 1.875rem;
      grid-auto-rows: 1fr;

      @include mobile {
        grid-auto-rows: auto;
      }
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
  .arrow {
    position: absolute;
    width: 6rem;
    height: 3rem;
    left: calc(50% - 3rem);
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    padding: 0;
    margin: 0;

    p {
      margin: 0;
      padding: 0;
    }
  }
</style>
