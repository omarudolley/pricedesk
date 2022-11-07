<script>
  import {
    Header,
    HeaderNav,
    HeaderNavItem,
    Dropdown,
    SkipToContent,
    Content
  } from 'carbon-components-svelte'
  import '../styles/index.scss'

  let isSideNavOpen = false
  $: innerWidth = 0
  $: isWideScreen = innerWidth >= 1056
  import { setLocation } from '$lib/stores'

  function setLocationCode(event) {
    const newIdentityId = event.detail.selectedId
    setLocation(newIdentityId)
  }
</script>

<svelte:window bind:innerWidth />

<div class="header-wrapper">
  <Header platformName="PriceDesk" bind:isSideNavOpen>
    <svelte:fragment slot="skip-to-content">
      <SkipToContent />
    </svelte:fragment>

    <Dropdown
      class="dropdowns"
      selectedId="dl"
      on:select={setLocationCode}
      items={[
        { id: 'dl', text: 'Duala' },
        { id: 'rl', text: 'Redlight' },
        { id: 'ws', text: 'Waterside' }
      ]}
    />
    <Dropdown
      class="dropdowns"
      selectedId="0"
      items={[
        { id: '0', text: 'USD' },
        { id: '1', text: 'LRD' }
      ]}
    />
    <HeaderNav>
      <HeaderNavItem href="faq" text="FAQ" />
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
    Proposals for additional features are welcome on our Github —
    https://github.com/omarudolley/pricedesk/issues
  </div>
</div>

<style lang="scss">
  $max-container-width: 105rem;

  .header-wrapper {
    background-color: #161616;
    width: 100%;
    position: fixed;
    z-index: 9000;
    top: 0;
    left: 0;
    right: 0;

    :global(header) {
      max-width: $max-container-width;
      margin: 0 auto;

      :global(.bx--header__name) {
        font-size: 1.5rem;
        @include mobile {
          font-size: 1.2rem;
        }
      }
      :global(.bx--header__nav) {
        display: flex;
        margin-left: auto;
        margin-right: 2rem;
        color: white;
        font-size: 1.2rem;

        @include mobile {
          margin: 0;
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
        color: white;
        font-size: 1.2rem;
        @include mobile {
          font-size: inherit;
        }
      }
      :global(.bx--list-box__menu-icon > svg) {
        fill: white;
      }
    }

    :global(.bx--form__helper-text) {
      margin: 0 1rem;
      color: #85fbc2;
      font-size: 0.8rem;
      @include mobile {
        font-size: inherit;
      }
    }
  }

  .layout {
    margin: 4rem auto 0 auto;
    max-width: $max-container-width;
    display: flex;
    flex-direction: column;
    min-height: 100vh;

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
  }

  .footer {
    display: flex;
    align-items: center;
    justify-content: center;
    background: $color-blue-light;

    margin-top: auto;
    padding: 2rem 0;
  }
</style>
