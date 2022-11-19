<script>
  import { currentLang, currentCurrency } from '$lib/stores'
  export let title
  export let priceListing
</script>

<div class="item">
  <div class="item_icon" />
  <div class="item_info">
    <p class="item-heading">{title[$currentLang]}</p>
    {#if title.en.startsWith('USD')}
      <p class="item_price">{priceListing[title.en]}</p>
    {:else}
      <p class="item_price">$ {priceListing[title.en]} {$currentCurrency.name}</p>
    {/if}
    <p
      class="item_change {priceListing[`${title.en}_change`] === 0
        ? 'neutral'
        : priceListing[`${title.en}_change`] > 0
        ? 'positive'
        : 'negative'}"
    >
      {priceListing[`${title.en}_change`] === 0
        ? '-'
        : priceListing[`${title.en}_change`] > 0
        ? priceListing[`${title.en}_change`]
        : Math.abs(priceListing[`${title.en}_change`])}
    </p>
  </div>
</div>

<style lang="scss">
  .item {
    position: relative;
    display: grid;
    grid-template-columns: 0.5rem auto;
    gap: 0.625rem;
    width: 100%;
    min-width: 13.75rem;
    max-width: 20rem;
    padding: 0.625rem;
    border-radius: 0.625rem;
    transition: all 0.8s cubic-bezier(0.075, 0.82, 0.165, 1) 0s;
    background: $color-background;
    cursor: pointer;

    .item_info {
      display: grid;
      gap: 8px;

      .item-heading {
        font-style: normal;
        font-size: 1rem;
        line-height: 1.12rem;
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
        font-style: normal;
        font-size: 1.5rem;
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
        font-style: normal;
        font-weight: normal;
        font-size: 0.8rem;
        line-height: 130%;
        position: absolute;
        width: 3rem;
        height: 1.25rem;
        background: $color-light-background;
        color: $color-black;
        border-radius: 0.3rem;
        text-align: center;
        margin: 0;
        padding-top: 2px;
        top: 0.625rem;
        right: 0.625rem;
      }

      .positive {
        color: $color-error;
        &::before {
          content: '\2191';
        }
      }
      .negative {
        color: $color-success;
        &::before {
          content: '\2193';
        }
      }
      .neutral {
        color: $color-neutral;
      }
    }
  }
</style>
