<script>
  export let title
  export let priceListing
</script>

<a class="wrapper">
  <div class="item">
    <div class="item_icon" />
    <div class="item_info">
      <p class="item-heading">{title}</p>
      {#if title.startsWith('USD')}
        <p class="item_price">{priceListing[title]}</p>
      {:else}
        <p class="item_price">$ {priceListing[title]}</p>
      {/if}

      <p
        class="item_change {priceListing[`${title}_change`] === 0
          ? 'neutral'
          : priceListing[`${title}_change`] > 0
          ? 'positive'
          : 'negative'}"
      >
        {priceListing[`${title}_change`]}
      </p>
    </div>
  </div>
</a>

<style lang="scss">
  .wrapper {
    text-decoration: none;
    width: 100%;
    background-color: transparent;
    border-radius: 0.3rem;
    &:link,
    &:visited,
    &:focus,
    &:hover,
    &:active {
      cursor: pointer;
      background: $color-light-background;
    }
  }

  .item {
    position: relative;
    display: grid;
    grid-template-columns: 46px auto;
    gap: 10px;
    width: 100%;
    min-width: 220px;
    max-width: 320px;
    padding: 10px;
    border-radius: 10px;
    transition: all 0.8s cubic-bezier(0.075, 0.82, 0.165, 1) 0s;

    .item_info {
      display: grid;
      gap: 8px;
      align-self: center;

      .item-heading {
        font-style: normal;
        font-size: 1rem;
        line-height: 1.12rem;
        max-width: 10rem;
        font-weight: 600;
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
        font-size: 1rem;
        line-height: 1rem;
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
          content: '+';
        }
      }
      .negative {
        color: $color-success;
      }
      .neutral {
        color: $color-neutral;
      }
    }
  }
</style>
