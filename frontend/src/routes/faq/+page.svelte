<script>
  import { faqs } from '$lib/data'
  import { Accordion, AccordionItem } from "carbon-components-svelte"
</script>

<div class="container">
  <div class="content">
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
