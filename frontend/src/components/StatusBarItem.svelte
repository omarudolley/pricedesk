<script>
  import { currentLang, currentCurrency } from '$lib/stores'
  import { websiteContent } from '$lib/data'
  import IncreaseLogo from '$lib/assets/increase.svg'
  import DecreaseLogo from '$lib/assets/decrease.svg'
  export let title
  export let priceListing
  export let setModal
</script>

<div class="item" on:click={setModal(title)}>
  <div class="item_icon" />
  <div class="item_info">
    <p class="item-heading">{title[$currentLang]}</p>
    {#if title.en.startsWith('USD')}
      <p class="item_price">{priceListing[title.en]}</p>
    {:else}
      <p class="item_price">$ {priceListing[title.en]} {$currentCurrency.name}</p>
    {/if}
    <div
      class="item_change {priceListing[`${title.en}_change`] === 0
        ? 'neutral'
        : priceListing[`${title.en}_change`] > 0
        ? 'positive'
        : 'negative'}"
    >
      {#if priceListing[`${title.en}_change`] === 0}{:else if priceListing[`${title.en}_change`] > 0}
        {priceListing[`${title.en}_change`]}
        <IncreaseLogo />
      {:else}
        {priceListing[`${title.en}_change`]}
        <DecreaseLogo />
      {/if}
    </div>
    {#if title.en.startsWith('USD')}
      <p class="last-recorded">
        {websiteContent.lastRecordedRate[$currentLang]}
        {priceListing[`${title.en}_last_recorded`]}
      </p>
    {:else}
      <p class="last-recorded">
        {websiteContent.lastRecordedPrice[$currentLang]} ${priceListing[
          `${title.en}_last_recorded`
        ]}
      </p>
    {/if}
  </div>
</div>

<style lang="scss">
  .item {
    margin: 0 auto;
    position: relative;
    display: grid;
    grid-template-columns: 0.5rem auto;
    gap: 0.625rem;
    width: 100%;
    min-width: 12rem;
    max-width: 20rem;
    padding: 0.625rem;
    border-radius: 0.2rem;
    transition: all 0.8s cubic-bezier(0.075, 0.82, 0.165, 1) 0s;
    background: white;
    cursor: pointer;

    &:hover {
      box-shadow: 0px 0px 6px rgba(0, 0, 0, 0.45);
      transform: scale(1.05);
    }

    .item_info {
      display: grid;
      gap: 8px;

      .item-heading {
        font-size: 1rem;
        line-height: 1.2rem;
        max-width: 10rem;
        color: $color-black;
        margin: 0;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        overflow: hidden;
        padding-right: 2.5rem;
      }

      .item_price {
        font-size: 1.2rem;
        line-height: 1.2rem;
        color: $color-black;
        margin: 0;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        overflow: hidden;
        font-weight: 600;
      }

      .item_change {
        display: flex;
        align-items: center;
        gap: 2px;
        font-size: 0.8rem;
        line-height: 130%;
        position: absolute;
        width: 4rem;
        height: 1.7rem;
        border-radius: 0.3rem;
        text-align: center;
        margin: 0;
        padding-top: 2px;
        top: 0.4rem;
        right: 0rem;
      }

      .last-recorded {
        font-size: 0.6rem;
        line-height: 0.8rem;
        max-width: 10rem;
        color: $color-black;
        margin: 0;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        overflow: hidden;
        padding-right: 2.5rem;
      }

      .positive {
        color: $color-success;
      }
      .negative {
        color: $color-error;
      }
      .neutral {
        color: $color-neutral;
      }
    }
  }
</style>
