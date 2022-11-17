<script>
  import { faqs } from '$lib/data'
  import { currentLang } from '$lib/stores'
  import { Accordion, AccordionItem } from 'carbon-components-svelte'
</script>

<div class="container">
  <div class="content">
    <h2 class="header">Questions fréquemment posées:</h2>
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
      margin-bottom: 2rem;
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

      .item {
        padding: 1.5rem;
      }
    }
  }
</style>
