<template>
  <div class="grid-container">
    <!-- <div class="grid-item"> -->
      <div class="grid-item1">
        Item-1
        <!-- <Navbar></Navbar> -->
      </div>
      <div class="grid-item2">
        Item-2
      </div>
      <div class="grid-item3">
        Item-3
      </div>
      <div class="grid-item4">
        Item-4
      </div>
      <div class="grid-item5">
        Item-5
      </div>
      <div class="grid-item6">
        Item-6
      </div>
      <div class="grid-item7">
        Item-7
      </div>
    <!-- </div> -->
  </div>
</template>

<script>
import { ref } from 'vue'
// import Navbar from '@/components/Navbar.vue'
import Sidebar from '@/components/Sidebar.vue'

const columns = [
  {
    name: 'name',
    required: true,
    label: 'Dessert (100g serving)',
    align: 'left',
    field: row => row.name,
    format: val => `${val}`,
    sortable: true
  },
  { name: 'calories', align: 'center', label: 'Calories', field: 'calories', sortable: true },
  { name: 'fat', label: 'Fat (g)', field: 'fat', sortable: true, style: 'width: 10px' },
  { name: 'carbs', label: 'Carbs (g)', field: 'carbs', sortable: true, },
  { name: 'protein', label: 'Protein (g)', field: 'protein' },
  { name: 'sodium', label: 'Sodium (mg)', field: 'sodium' },
  { name: 'calcium', label: 'Calcium (%)', field: 'calcium', sortable: true, sort: (a, b) => parseInt(a, 10) - parseInt(b, 10) },
  { name: 'iron', label: 'Iron (%)', field: 'iron', sortable: true, sort: (a, b) => parseInt(a, 10) - parseInt(b, 10) }
]

const rows = [
  {
    name: 'Frozen Yogurt',
    calories: 159,
    fat: 6.0,
    carbs: 24,
    protein: 4.0,
    sodium: 87,
    calcium: '14%',
    iron: '1%'
  },
  {
    name: 'Ice cream sandwich',
    calories: 237,
    fat: 9.0,
    carbs: 37,
    protein: 4.3,
    sodium: 129,
    calcium: '8%',
    iron: '1%'
  },
  {
    name: 'Eclair',
    calories: 262,
    fat: 16.0,
    carbs: 23,
    protein: 6.0,
    sodium: 337,
    calcium: '6%',
    iron: '7%'
  },
  {
    name: 'Cupcake',
    calories: 305,
    fat: 3.7,
    carbs: 67,
    protein: 4.3,
    sodium: 413,
    calcium: '3%',
    iron: '8%'
  },
  {
    name: 'Gingerbread',
    calories: 356,
    fat: 16.0,
    carbs: 49,
    protein: 3.9,
    sodium: 327,
    calcium: '7%',
    iron: '16%'
  },
  {
    name: 'Jelly bean',
    calories: 375,
    fat: 0.0,
    carbs: 94,
    protein: 0.0,
    sodium: 50,
    calcium: '0%',
    iron: '0%'
  },
  {
    name: 'Lollipop',
    calories: 392,
    fat: 0.2,
    carbs: 98,
    protein: 0,
    sodium: 38,
    calcium: '0%',
    iron: '2%'
  },
  {
    name: 'Honeycomb',
    calories: 408,
    fat: 3.2,
    carbs: 87,
    protein: 6.5,
    sodium: 562,
    calcium: '0%',
    iron: '45%'
  },
  {
    name: 'Donut',
    calories: 452,
    fat: 25.0,
    carbs: 51,
    protein: 4.9,
    sodium: 326,
    calcium: '2%',
    iron: '22%'
  },
  {
    name: 'KitKat',
    calories: 518,
    fat: 26.0,
    carbs: 65,
    protein: 7,
    sodium: 54,
    calcium: '12%',
    iron: '6%'
  }
]

export default {
  components: {
    // Navbar,
    Sidebar,
  },
  setup () {
    return {
      columns,
      rows: ref(rows)
    }
  }
}
</script>

<style>

.grid-container {
  display: grid;
  grid-template-columns: minmax(200px, 200px) auto minmax(150px, 200px);
  grid-template-rows: 40px 40px auto 40px;
  height: 100vh;
  width: 100%;
  border: 2px solid rgb(197, 56, 21);
  gap: 2px
}

.grid-item {
  border: 5px solid rgb(73, 100, 0);
}

.grid-item1 {
  /* position: fixed; */
  grid-column: 1/4;
  grid-row: 1/2;
  background-color: rgba(165, 42, 42, 0.336);
}

.grid-item2 {
  
  grid-column: 1/2;
  grid-row: 2/4;
  background-color: rgba(42, 165, 159, 0.336);
}

.grid-item3 {
  grid-column: 2/3;
  grid-row: 2/3;
  background-color: rgba(165, 42, 165, 0.336);
}

.grid-item4 {
  grid-column: 3/4;
  grid-row: 2/3;
  background-color: rgba(116, 42, 165, 0.336);
}

.grid-item5 {
  grid-column: 2/3;
  grid-row: 3/4;
  background-color: rgba(165, 42, 73, 0.336);
}

.grid-item6 {
  grid-column: 3/4;
  grid-row: 3/4;
  background-color: rgba(87, 165, 42, 0.336);
}

.grid-item7 {
  grid-column: 1/4;
  grid-row: 4/5;
  background-color: rgba(142, 165, 42, 0.336);
}

.logo {
  display: block;
}

</style>