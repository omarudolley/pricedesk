<script>
  import { faqs } from '$lib/data'
  import { currentLang } from '$lib/stores'
  import FAQ from '$components/FAQ.svelte'
  import { Button } from 'carbon-components-svelte'
</script>

<div class="container">
  <div class="content">
    <h2 class="header">
      {#if $currentLang === 'en'}Frequently asked questions:{:else}Questions fréquemment posées:{/if}
    </h2>

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
    background: $color-primary;
    padding: 1rem;

    @include mobile {
      padding: 1rem;
    }

    .header {
      font-weight: 600;
      padding: 1rem;

      @include mobile {
        font-size: 1rem;
      }
    }

    .content {
      display: flex;
      flex-direction: column;
      max-width: $container-max-width;
      gap: 1rem;

      .button {
        margin-left: auto;
        padding: 1rem;
      }
    }
  }
</style>
