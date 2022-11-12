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
    padding: 2rem;

    .content {
      display: flex;
      flex-direction: column;
      max-width: 80rem;
      .item {
        padding: 1rem;
      }
    }
  }
</style>
