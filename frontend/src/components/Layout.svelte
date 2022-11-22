<script>
  import {
    Header,
    HeaderNav,
    HeaderNavItem,
    SkipToContent,
    Content
  } from 'carbon-components-svelte'
  import LanguageSelector from '$components/LanguageSelector.svelte'
  import { base } from '$app/paths'
  import { websiteContent } from '$lib/data'
  let isSideNavOpen = false
  $: innerWidth = 0
  $: isWideScreen = innerWidth >= 1056
  import { setCurrency, currentListing, currentLang } from '$lib/stores'

  let selected
  $: {
    setCurrency(selected)
  }
</script>

<svelte:window bind:innerWidth />

<div class="header-wrapper">
  <Header company="Liberia" platformName="MarketIndex" bind:isSideNavOpen href="/">
    <svelte:fragment slot="skip-to-content">
      <SkipToContent />
    </svelte:fragment>
    {#if $currentListing && typeof $currentListing !== 'undefined'}
      <p class="last-update">{websiteContent.update[$currentLang]} {$currentListing.updatedOn}</p>
    {/if}

    <select class="currency" bind:value={selected}>
      <option value={'usd'}> USD </option>
      <option value={'lrd'}> LRD </option>
    </select>

    <HeaderNav>
      <HeaderNavItem href="{base}/faq" text="FAQ" />
    </HeaderNav>
    <LanguageSelector />
  </Header>
</div>

<div class="layout" class:is-wide-screen={isWideScreen}>
  <div class="content-wrapper">
    <Content>
      <div class="main">
        <slot />
      </div>
    </Content>
  </div>
  <div class="footer">
    {websiteContent.footer[$currentLang]} —

    <a href="https://github.com/omarudolley/pricedesk/issues" target="_blank">
      https://github.com/omarudolley/pricedesk/issues
    </a>
  </div>
</div>

<style lang="scss">
  @import 'src/styles/index.scss';
  $max-container-width: 105rem;

  .header-wrapper {
    width: 100%;
    position: fixed;
    z-index: 9000;
    top: 0;
    left: 0;
    right: 0;
    background: white;

    color: black;
    :global(header) {
      max-width: $container-max-width;
      margin: 0 auto;
      background: white;
      color: black;

      :global(.bx--header__name) {
        color: black;
        font-size: 1.5rem;
        @include mobile {
          font-size: 1rem;
          max-width: 6rem;
        }
      }
      :global(.bx--header__nav) {
        font-weight: 600;
        display: flex;
        margin-left: auto;
        font-size: 1.2rem;

        :global(.bx--header__menu-item) {
          padding: 0.5rem;
          color: black;
          &:hover {
            color: black;
            background: white;
          }
        }

        @include mobile {
          margin-left: 0.5rem;
          padding: 0;
          font-size: inherit;
        }
      }
    }
  }

  .layout {
    margin: 4rem auto 0 auto;
    max-width: $max-container-width;
    display: flex;
    flex-direction: column;
    min-height: 100vh;
    background: white;

    .content-wrapper {
      display: flex;
      min-height: 100%;
      margin-bottom: 2rem;
    }
  }

  :global(header.bx--header) {
    position: relative;
  }

  :global(.layout.is-wide-screen nav.bx--side-nav) {
    position: sticky;
    flex-shrink: 0;
  }

  :global(.bx--side-nav ~ .bx--content) {
    margin-left: 0;
  }

  :global(.bx--side-nav.bx--side-nav--expanded ~ .bx--content) {
    margin-left: 0;
  }

  :global(.bx--side-nav.bx--side-nav--collapsed) {
    position: fixed;
  }

  :global(.bx--header) {
    height: 4rem;
  }

  :global(.bx--header ~ .bx--side-nav) {
    top: 4rem;
  }
  :global(.bx--content) {
    @include mobile {
      padding: 0;
      margin-left: 0 !important;
    }
  }

  :global(.bx--content) {
    width: 100%;
    min-height: 100%;
  }

  .main {
    min-height: 100%;
    max-width: $container-max-width;
    width: 100%;
    margin: auto;
  }

  .footer {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;

    background: $color-background;

    margin-top: auto;
    padding: 2rem 0.5rem;

    @include mobile {
      font-size: 0.8rem;
    }
  }

  .last-update {
    position: absolute;
    top: 3rem;
    left: 1.2rem;
    color: black;
    font-size: 0.6rem;
  }
  .currency {
    border: none;
    color: black;
    @include mobile {
      margin-left: 5rem;
    }
  }
</style>
