<script>
  import StatusBar from '$components/StatusBar.svelte'
</script>

<div class="container">
  <StatusBar />
</div>

<style lang="scss">
  .container {
    display: flex;
    align-items: center;
    justify-content: center;
    @include mobile {
      padding: 1rem;
    }
  }
</style>
