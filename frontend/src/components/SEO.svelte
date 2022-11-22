<script lang="ts">
  export let title: string | undefined = undefined
  export let websiteName = 'Liberia MarketIndex'
  export let description = 'Liberia MarketIndex'
  export let lang = 'en'
  export let keywords: string | undefined = undefined
  export let image: string | undefined = undefined

  const pageTitle = title ? `${title} | ${websiteName}` : websiteName
</script>

<svelte:head>
  <title>{pageTitle}</title>
  <meta name="description" content={description} />
  <meta name="keywords" content={keywords} />
  <meta name="robots" content="index, follow" />

  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <meta property="og:site_name" content={websiteName} />
  <meta property="og:locale" content={lang} />
  <meta property="og:type" content={'website'} />
  <meta property="og:title" content={pageTitle} />
  <meta property="og:description" content={description} />

  {#if image}
    <meta property="og:image" itemprop="image" content={image} />
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="627" />
  {/if}
</svelte:head>
