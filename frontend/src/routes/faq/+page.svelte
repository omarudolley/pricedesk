<script>
  import { faqs } from '$lib/data'
</script>

<div class="container">
  <div class="content">
    {#each faqs as item}
      <div class="item">
        <h5>
          {item.question}
        </h5>
        <p>
          {item.answer}
        </p>
      </div>
    {/each}
  </div>
</div>

<style lang="scss">
  .container {
    display: flex;
    flex-direction: column;

    .content {
      display: flex;
      flex-direction: column;
      max-width: $container-max-width;
      .item {
        padding: 1.5rem;
      }
    }
  }
</style>
