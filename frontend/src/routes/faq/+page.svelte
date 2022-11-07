<script>
  import { faqs } from '$lib/data'
</script>

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

<style lang="scss">
  .content {
    display: flex;
    .item {
      padding: 1rem;
    }
  }
</style>
