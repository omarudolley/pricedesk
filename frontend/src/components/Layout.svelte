<script>
  import {
    Header,
    HeaderNav,
    HeaderNavItem,
    Dropdown,
    SkipToContent,
    Content,
    HeaderNavMenu
  } from 'carbon-components-svelte'
  import { base } from '$app/paths'
  import { page } from '$app/stores'
  import { websiteContent } from '$lib/data'

  let isSideNavOpen = false
  $: innerWidth = 0
  $: isWideScreen = innerWidth >= 1056
  import { setCurrency, currentListing, currentLang } from '$lib/stores'

  function setCurrencyCode(event) {
    const newIdentityId = event.detail.selectedId
    setCurrency(newIdentityId)
  }

  $: {
    currentLang.set($page.url.hash.substring(1, 3))
  }
</script>

<svelte:window bind:innerWidth />

<div class="header-wrapper">
  <Header company="Liberia" platformName="MarketIndex" bind:isSideNavOpen href="/#{$currentLang}">
    <svelte:fragment slot="skip-to-content">
      <SkipToContent />
    </svelte:fragment>
    {#if $currentListing && typeof $currentListing !== 'undefined'}
      <p class="last-update">{websiteContent.update[$currentLang]} {$currentListing.updatedOn}</p>
    {/if}
    <Dropdown
      class="dropdowns"
      selectedId="usd"
      on:select={setCurrencyCode}
      items={[
        { id: 'usd', text: 'USD' },
        { id: 'lrd', text: 'LRD' }
      ]}
    />

    <HeaderNav>
      <HeaderNavItem href="{base}/faq/{$page.url.hash}" text="faq" />
      <HeaderNavMenu text={$page.url.hash.substring(1, 3) || 'en'}>
        <HeaderNavItem href="#en" text="en" />
        <HeaderNavItem href="#fr" text="fr" />
      </HeaderNavMenu>
    </HeaderNav>
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
    background: $color-background;

    color: black;
    :global(header) {
      max-width: $container-max-width;
      margin: 0 auto;
      background: $color-background;
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
        margin-right: 2rem;

        font-size: 1.2rem;
        :global(.bx--header__menu) {
          width: 4.5rem;

          color: black;
          background: $color-background;
          :global(.bx--header__menu-item) {
            color: black;
            &:hover,
            &:focus {
              text-decoration: underline;
              background: $color-background;
            }
          }
        }
        :global(.bx--header__menu-title) {
          width: 4rem;
          background: $color-background;
          color: black;
        }
        :global(.bx--header__menu-title > svg) {
          fill: black;
          &:hover,
          &:focus {
            fill: black;
          }
        }
        :global(.bx--header__submenu) {
          color: black;
          background: $color-background;
          &:hover,
          &:focus {
            color: black;
            background: $color-background;
          }
        }
        :global(.bx--header__menu-item) {
          color: black;
          &:hover {
            color: black;
            background: $color-background;
          }
        }

        @include mobile {
          margin-right: auto;
          padding: 0;
          font-size: inherit;
        }
      }
    }
  }

  :global(.dropdowns) {
    :global(.bx--dropdown) {
      background-color: transparent;
      border-bottom: none;
      height: auto;

      :global(.bx--list-box__field) {
        height: auto;
      }
      :global(.bx--list-box__label) {
        color: black;
        font-size: 1.2rem;
        @include mobile {
          font-size: inherit;
        }
      }
      :global(.bx--list-box__menu-icon > svg) {
        fill: black;
      }
    }

    @include mobile {
      margin-left: 5rem;
    }
  }

  .layout {
    margin: 4rem auto 0 auto;
    max-width: $max-container-width;
    display: flex;
    flex-direction: column;
    min-height: 100vh;
    background: $color-background;

    .content-wrapper {
      display: flex;
      min-height: 100%;
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
    padding: 2rem 0;

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
</style>
