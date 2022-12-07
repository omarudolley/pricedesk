<script>
  import { faqs } from '$lib/data'
  import { currentLang } from '$lib/stores'
  import FAQ from '$components/FAQ.svelte'
  import { Button } from 'carbon-components-svelte'
</script>

<div class="container">
  <div class="content">
    <div class="header">
      {#if $currentLang === 'en'}Frequently asked questions:{:else}Questions fréquemment posées:{/if}
    </div>
    <div class="underline">
      <hr />
    </div>

    {#if $currentLang}
      {#each faqs[$currentLang] as item}
        <FAQ question={item.question} answer={item.answer} />
      {/each}
    {/if}

    <div class="button">
      <Button kind="secondary" href="/">Back</Button>
    </div>
  </div>
</div>

<style lang="scss">
  .container {
    display: flex;
    flex-direction: column;

    padding: 1rem;

    @include mobile {
      padding: 1rem;
    }

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

    .content {
      background: $color-primary;
      display: flex;
      flex-direction: column;
      max-width: $container-max-width;
      gap: 1rem;
      padding: 1rem;

      .button {
        margin-left: auto;
      }
    }
  }
  hr {
    color: white;
  }
</style>
