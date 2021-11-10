<template>
<form @submit="onSubmit" class="add-form">
    <div class="border p-2 rounded w-1/2 flex flex-col justify-between h-96 w-96">
        <div class="flex flex-col">
            <div>
  <p v-for="message in messages" :key="message">{{ message }}</p>
</div>
        </div>
        <input class="border rounded p-2" type="text" v-model="text" placeholder="Chat here" />
         <input type="submit" value="Send message" class="btn btn-block" />

    </div>
</form>
</template>

<script>

export default {

name: 'Chatbox',
data() {
	return {
     messages: [],
	text: '',
    }

},


methods: {

     getMessages(message) {
        this.messages = [... this.messages, message]
},

    onSubmit(e) {
	e.preventDefault()

	if(!this.text) {
	alert('Please add a comment')
	return
	}

   this.getMessages(this.text)

    this.text = ''

    }
}
}
</script>