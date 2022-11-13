<script>
  export let title
  export let priceListing
</script>

<div class="item">
  <div class="item-heading">
    <strong>{title}</strong>
  </div>
  <h2>{priceListing[title]}</h2>
  <strong
    class="{priceListing[title] === 0
      ? 'neutral'
      : priceListing[title] > 0
      ? 'positive'
      : 'negative'} "
  >
    {priceListing[`${title}_change`]}
  </strong>
</div>

<style lang="scss">
  .item {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    .item-heading {
      display: flex;
      align-items: center;
      justify-content: center;
      height: 6em;
      margin-bottom: -0.4em;
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

  strong {
    font-size: 1.2rem;
    font-weight: 500;
    margin-top: 0;
    margin-bottom: 0.5rem;
    line-height: 1.2;
    display: block;
  }
</style>
