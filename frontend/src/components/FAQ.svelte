<script>
  import PlusLogo from '$lib/assets/plus.svg'
  import MinusLogo from '$lib/assets/minus.svg'
  import ArrowUp from '$lib/assets/arrowup.svg'

  let open = false

  export let question
  export let answer
</script>

<div class="faq__container">
  <div class="faq__question" on:click={() => (open = !open)}>
    <div>
      {question}
    </div>
    <div class="faq__question_opener">
      {#if open}
        <MinusLogo />
      {:else}
        <PlusLogo />
      {/if}
    </div>
  </div>
  {#if open}
    <div class="faq__answer">
      {@html answer}
      <div class="arrow-up" on:click={() => (open = !open)}>
        <ArrowUp />
      </div>
    </div>
  {/if}
</div>

<style lang="scss">
  .faq__container {
    display: flex;
    flex-direction: column;

    .faq__question {
      display: flex;
      padding: 2rem;
      justify-content: space-between;
      cursor: pointer;
      font-size: 1.3rem;

      background: white;
      .faq__question_opener {
        cursor: pointer;
      }
    }

    .faq__answer {
      padding: 2rem;
      margin: 0.1rem 0;
      font-size: 1.1rem;

      background: white;

      .arrow-up {
        margin-left: auto;
        display: flex;
        justify-content: flex-end;
        align-items: flex-end;
        padding: 5rem 0rem 0.2rem 0;

        svg {
          cursor: pointer;
        }
      }
    }
  }
</style>
