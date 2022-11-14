<script>
  import StatusBar from '$components/StatusBar.svelte'
</script>

<div class="container">
  <StatusBar />
</div>

<style lang="scss">
  .container {
    @include mobile {
      padding: 1rem;
    }
  }
</style>
