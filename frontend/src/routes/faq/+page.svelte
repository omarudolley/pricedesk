<script>
  import { faqs } from '$lib/data'
  import { Accordion, AccordionItem } from 'carbon-components-svelte'
</script>

<div class="container">
  <div class="content">
    <h2 class="header">Frequently asked questions:</h2>
    <Accordion size="xl">
      {#each faqs as item}
        <AccordionItem title={item.question}>
          <p>
            {item.answer}
          </p>
        </AccordionItem>
      {/each}
    </Accordion>
  </div>
</div>

<style lang="scss">
  .container {
    display: flex;
    flex-direction: column;
    padding: 1rem;
    

    .header {
      margin-bottom: 2rem;
      padding: 1.5rem;
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
