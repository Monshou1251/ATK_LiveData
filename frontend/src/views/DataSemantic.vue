<template>
  <section>
    <div class="ui segment grey signup-form"></div>
    <div>
      <sui-table-header>
        <sui-table-row>
          <sui-table-header-cell>Name</sui-table-header-cell>
          <sui-table-header-cell>Status</sui-table-header-cell>
          <sui-table-header-cell>Notes</sui-table-header-cell>
        </sui-table-row>
      </sui-table-header>
    </div>
  </section>
    <!-- <sui-table selectable celled>
      <sui-table-header>
        <sui-table-row>
          <sui-table-header-cell>Name</sui-table-header-cell>
          <sui-table-header-cell>Status</sui-table-header-cell>
          <sui-table-header-cell>Notes</sui-table-header-cell>
        </sui-table-row>
      </sui-table-header>
      <sui-table-body>
        <sui-table-row>
          <sui-table-cell>John</sui-table-cell>
          <sui-table-cell>No Action</sui-table-cell>
          <sui-table-cell>None</sui-table-cell>
        </sui-table-row>
        <sui-table-row>
          <sui-table-cell>Jamie</sui-table-cell>
          <sui-table-cell>Approved</sui-table-cell>
          <sui-table-cell>Requires call</sui-table-cell>
        </sui-table-row>
        <sui-table-row>
          <sui-table-cell>Jill</sui-table-cell>
          <sui-table-cell>Denied</sui-table-cell>
          <sui-table-cell>None</sui-table-cell>
        </sui-table-row>
        <sui-table-row warning>
          <sui-table-cell>John</sui-table-cell>
          <sui-table-cell>No Action</sui-table-cell>
          <sui-table-cell>None</sui-table-cell>
        </sui-table-row>
        <sui-table-row>
          <sui-table-cell>Jamie</sui-table-cell>
          <sui-table-cell positive>Approved</sui-table-cell>
          <sui-table-cell warning>Requires call</sui-table-cell>
        </sui-table-row>
        <sui-table-row>
          <sui-table-cell>Jill</sui-table-cell>
          <sui-table-cell negative>Denied</sui-table-cell>
          <sui-table-cell>None</sui-table-cell>
        </sui-table-row>
      </sui-table-body>
    </sui-table> -->
</template>
  
<script>
export default {
  name: 'DataSemantic',
};
</script>

<style>
  section {
    height: 100vh;
    background: rgb(238,174,202);
    background: radial-gradient(circle, rgba(238,174,202,1) 0%, rgba(148,187,233,1) 100%);
  }
</style>