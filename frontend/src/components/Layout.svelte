<script>
  import {
    Header,
    HeaderNav,
    HeaderNavItem,
    HeaderNavMenu,
    SkipToContent,
    Content,
    SideNav,
    SideNavLink,
    SideNavMenu,
    SideNavItems,
    SideNavMenuItem
  } from 'carbon-components-svelte'
  import '../styles/index.scss'

  let isSideNavOpen = false
  $: innerWidth = 0
  $: isWideScreen = innerWidth >= 1056
</script>

<svelte:window bind:innerWidth />

<div class="header-wrapper">
  <Header platformName="PriceDesk" bind:isSideNavOpen persistentHamburgerMenu={true}>
    <svelte:fragment slot="skip-to-content">
      <SkipToContent />
    </svelte:fragment>
    <HeaderNav>
      <HeaderNavItem href="/" text="FAQ" />
      <HeaderNavMenu text="Currency">
        <HeaderNavItem href="/" text="USD" />
        <HeaderNavItem href="/" text="LRD" />
      </HeaderNavMenu>

      <HeaderNavMenu text="Locations">
        <HeaderNavItem href="/" text="Red Light" />
        <HeaderNavItem href="/" text="Waterside" />
        <HeaderNavItem href="/" text="Duala" />
      </HeaderNavMenu>
    </HeaderNav>
  </Header>
</div>

<div class="layout" class:is-wide-screen={isWideScreen}>
  <div class="content-wrapper">
    <SideNav bind:isOpen={isSideNavOpen}>
      <SideNavItems>
        <SideNavLink href="/" text="FAQ" />

        <SideNavMenu text="Currency">
          <SideNavMenuItem href="/" text="USD" />
          <SideNavMenuItem href="/" text="LRD" />
        </SideNavMenu>

        <SideNavMenu text="Locations">
          <SideNavMenuItem href="/" text="Red Light" />
          <SideNavMenuItem href="/" text="Waterside" />
          <SideNavMenuItem href="/" text="Duala" />
        </SideNavMenu>
      </SideNavItems>
    </SideNav>
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
    }
  }

  .layout {
    margin: 4rem auto 0 auto;
    max-width: $max-container-width;
    display: flex;
    flex-direction: column;
    min-height: calc(100vh - 3rem);

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