<script>
  import Layout from '$components/Layout.svelte'
  import SEO from '$components/SEO.svelte'
  import Image from '$lib/assets/og.jpeg'
</script>

<SEO
  description="Market Index aims to provide accurate and up-to-date information about the price of basis
commodities in Liberia."
  keywords="Liberia, Market, prices, commodities, inflation"
  image={Image}
/>
<Layout>
  <slot />
</Layout>
