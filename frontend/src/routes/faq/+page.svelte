<script>
  import { faqs } from '$lib/data'
  import { currentLang } from '$lib/stores'
  import { Accordion, AccordionItem, Button } from 'carbon-components-svelte'
  import ArrowLeft from 'carbon-icons-svelte/lib/ArrowLeft.svelte'
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
              {item.answer}
            </p>
          </AccordionItem>
        {/each}
      {/if}
    </Accordion>
    <div class="button">
      <Button kind="secondary" icon={ArrowLeft} tooltipPosition="right" href="/">Back</Button>
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
        padding: 1rem;
      }
    }
  }
</style>
