<script>
  import { faqs } from '$lib/data'
  import { currentLang } from '$lib/stores'
  import { Accordion, AccordionItem, Button } from 'carbon-components-svelte'
</script>

<div class="container">
  <div class="content">
    <h2 class="header">
      {#if $currentLang === 'en'}Frequently asked questions:{:else}Questions fréquemment posées:{/if}
    </h2>
    <Accordion size="xl">
      {#if $currentLang}
        {#each faqs[$currentLang] as item}
          <AccordionItem title={item.question}>
            <p>
              {@html item.answer}
            </p>
          </AccordionItem>
        {/each}
      {/if}
    </Accordion>
    <div class="button">
      <Button kind="secondary" href="/">Back</Button>
    </div>
  </div>
</div>

<style lang="scss">
  .container {
    display: flex;
    flex-direction: column;

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
      gap: 2rem;

      .item {
        padding: 1.5rem;
      }
      .button {
        margin-left: auto;
        padding: 1rem;
      }
    }

    :global(.bx--btn) {
      background: #0f62fe;
    }
  }
</style>
