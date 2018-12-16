<template>
  <section class="section">
    <div class="container">
      <div class="selector">
        <div class="level">
            <div class="level-item">
                Berapa paragraf?
            </div>
            <div class="level-item">
                <b-field>
                    <b-select
                        size="is-medium"
                        v-model="n"
                        >
                        <option value="3">3</option>
                        <option value="5">5</option>
                        <option value="10">10</option>
                    </b-select>
                </b-field>
            </div>
        </div>
      </div>
      
      <div class="output">
        <span style="white-space: pre-wrap;">{{ text }}</span>
      </div>

    </div>
  </section>

  
</template>

<script src="https://cdn.jsdelivr.net/npm/lodash@4.13.1/lodash.min.js"></script>
<script>
import axios from 'axios'
import _ from 'lodash'
export default {
  data () {
    return {
      n: 3,
      text: this.getText()
    }
  },
  watch: {
    n: function (newN, oldN) {
      this.getText()
    }
  },
  methods: {
    getText: _.debounce(
      function () {
        let params = {}
        params['n'] = this.n
        const path = `http://127.0.0.1:5000/api/maknyus`
        axios.get(path, {
          params: params
        })
        .then(response => {
          this.text = response.data.text
        })
        .catch(error => {
          this.text = ''
          console.log(error)
        })
      },
      500
    )
  }
}
</script>
