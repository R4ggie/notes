<template>
  <content class="data">
    <div class="font-light" style="background: #2b2b28">
      <div class="container">
        <h1>Notes Library</h1>
      </div>
      <b-alert v-if="showMsg" show>{{ msg }}</b-alert>
      <div class="container">
        <button class="btn-cls" @click="showModal">Add Note</button>
      </div>
      <div class="center">
        <table>
          <thead>
            <tr>
              <th>Note</th>
              <th>Label</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(note, index) in notes" :key="index">
              <td>{{ note.note }}</td>
              <td>{{ note.label }}</td>
              <td>
                <div class="group">
                  <button type="button" class="btn-tb" @click="deleteNote(note)">Delete</button>
                  <button type="button" class="btn-tb" @click="showUpdateModal(note)">
                    Update
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <footer>
        <div class="container">
          <p>For more projects</p>
          <a href="https://github.com/R4ggie">R@ggie</a>
        </div>
      </footer>
    </div>

    <b-modal ref="addNoteModal" id="note-modal" title="Add a new Note" hide-backdrop hide-footer>
      <b-form @submit="onSubmit" class="w-100">
        <b-form-group id="form-note-group" label="Note:" label-for="form-note-input">
          <b-form-input
            id="form-note-input"
            type="text"
            v-model="addNoteForm.note"
            required
            placeholder="Enter Note"
          ></b-form-input>
        </b-form-group>

        <b-form-group id="form-label-group" label="Label:" label-for="form-label-input">
          <b-form-input
            id="form-label-input"
            type="text"
            v-model="addNoteForm.label"
            required
            placeholder="Enter Label"
          ></b-form-input>
        </b-form-group>

        <b-button type="submit">Submit</b-button>
      </b-form>
    </b-modal>

    <b-modal
      ref="updateNoteModal"
      id="update-note-modal"
      title="Update Note"
      hide-backdrop
      hide-footer
    >
      <b-form @submit="onUpdateSubmit" class="w-100">
        <b-form-group id="form-update-note-group" label="Note:" label-for="form-update-note-input">
          <b-form-input
            id="form-update-note-input"
            type="text"
            v-model="updateNoteForm.note"
            required
            placeholder="Enter Note"
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="form-update-label-group"
          label="Label:"
          label-for="form-update-label-input"
        >
          <b-form-input
            id="form-update-label-input"
            type="text"
            v-model="updateNoteForm.label"
            required
            placeholder="Enter Label"
          ></b-form-input>
        </b-form-group>

        <b-button type="submit">Submit</b-button>
      </b-form>
    </b-modal>
  </content>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      notes: [],

      addNoteForm: {
        note: '',
        label: ''
      },
      updateNoteForm: {
        id: '',
        note: '',
        label: ''
      },
      showMsg: false, // Make sure this is initialized
      msg: ''
    }
  },

  methods: {
    showModal() {
      this.$refs.addNoteModal.show()
    },
    showUpdateModal(note) {
      this.updateNoteForm.id = note.id
      this.updateNoteForm.note = note.note
      this.updateNoteForm.label = note.label
      this.$refs.updateNoteModal.show()
    },
    getNotes() {
      const path = 'http://localhost:5000/notepage'
      axios.get(path).then((res) => {
        //res is short for response//then means do this with the response
        console.log(res.data) //res = return from app.py // shhows us in logs
        this.notes = res.data.notes //res.data contains the respnse from backend and stores it in msg
      })
    },
    addNote(payLoad) {
      const path = 'http://localhost:5000/notepage'
      axios.post(path, payLoad).then(() => {
        this.getNotes() //places the new text in getnote func
        this.msg = 'Note Added'
        this.showMsg = true
        setTimeout(() => {
          this.showMsg = false // Hide the message after 3 seconds
        }, 3000)
      })
    },
    updateNote() {
      const path = `http://localhost:5000/notepage/${this.updateNoteForm.id}`
      axios.put(path, this.updateNoteForm).then(() => {
        this.getNotes()
        this.msg = 'Note Updated!'
        this.showMsg = true
        setTimeout(() => {
          this.showMsg = false
        }, 3000)
      })
    },
    initForm() {
      this.addNoteForm.note = ''
      this.addNoteForm.label = ''
    },
    onSubmit(e) {
      e.preventDefault()
      this.$refs.addNoteModal.hide()
      const payLoad = {
        note: this.addNoteForm.note,
        label: this.addNoteForm.label
      }
      this.addNote(payLoad)
      this.initForm()
    },
    onUpdateSubmit(e) {
      e.preventDefault()
      this.$refs.updateNoteModal.hide()
      this.updateNote()
    },
    removeNote(note_id) {
      const path = `http://localhost:5000/notepage/${note_id}`
      axios.delete(path).then(() => {
        this.getNotes() //places the new text in getnote func
        this.msg = 'Note Deleted!'
        this.showMsg = true
        setTimeout(() => {
          this.showMsg = false
        }, 3000)
      })
    },
    deleteNote(note) {
      this.removeNote(note.id) //when we click run this
    }
  },

  created() {
    this.getNotes() //runs the getNotes func before the page loads cz it wont run unless with this or a button
  }
}
</script>
<!-- stores the responde to  "notes" as a list -->
<!--  the funcion we made will sends a GET request using axios path, gets a response then stores it in notes list-->
<!-- then in our template we used for loop to add colooms as much as the notes in the list -->
<!-- then usiing the {{ var }}  we set inside it which data either the note or the label-->
