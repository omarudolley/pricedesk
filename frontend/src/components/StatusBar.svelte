<script>
  import { currentListing, currentLang } from '$lib/stores'
  import RenderStatusItem from '$components/RenderStatusItem.svelte'
  import { commodities, websiteContent } from '$lib/data'

  import MdKeyboardArrowDown from 'svelte-icons/md/MdKeyboardArrowDown.svelte'
  import MdKeyboardArrowUp from 'svelte-icons/md/MdKeyboardArrowUp.svelte'

  let miniList = commodities.slice(1, 13)
  $: listingToRender = miniList
  let toggleDownArrow

  function showOrHideMore() {
    listingToRender = toggleDownArrow ? miniList : commodities
    toggleDownArrow = !toggleDownArrow
  }
</script>

<div class="wrapper">
  {#if $currentListing && typeof $currentListing !== 'undefined'}
    {@const priceListing = Object.freeze($currentListing)}
    <div class="inner top">
      <div class="header">{websiteContent.intro[$currentLang]}</div>
      <RenderStatusItem title={{ en: 'USD buying rate', fr: "USD taux d'achat" }} {priceListing} />
      <RenderStatusItem title={{ en: 'USD buying rate', fr: 'USD taux de vente' }} {priceListing} />
    </div>
    <div class="underline">
      <hr />
    </div>

    <div class="inner bottom">
      {#each listingToRender as title}
        <RenderStatusItem {title} {priceListing} />
      {/each}
    </div>
  {/if}
  <div class="arrow" on:click={showOrHideMore}>
    {#if toggleDownArrow}
      <MdKeyboardArrowUp />
      <p>{websiteContent.less[$currentLang]}</p>
    {:else}
      <MdKeyboardArrowDown />
      <p>{websiteContent.more[$currentLang]}</p>
    {/if}
  </div>
</div>

<style lang="scss">
  .wrapper {
    background: #8fc2ff;
    border-radius: 1.25rem;
    position: relative;

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
