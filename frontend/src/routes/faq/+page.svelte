<script>
  import { faqs } from '$lib/data'
</script>

<div class="container">
  <h1>Welcome to FAQ</h1>
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
    align-items: center;
    justify-content: center;
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
