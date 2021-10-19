<template>
  <div>
    <b-alert
      :variant="alter_variant"
      show
    >
      {{ message }}
    </b-alert>
    <br>
  </div>
</template>

<script>
export default {
  props: ['message', 'alterVariant'],
};
</script>
