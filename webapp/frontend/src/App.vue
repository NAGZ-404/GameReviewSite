<template>
  <meta charset="UTF-8">

  <h1> My Game Reviews App</h1>
  <div>
    <!-- Form for posting a review -->
    <div class="mb-3">
      <div>
        <!-- <button> Post a Game Review</button> -->
        <div>
          <form name="gameReview-form" method="POST" class = "card p-3 bg-light" >
            <div class="form-group m-1">
              <label for="title">Title</label>
              <input class="form-control " type="text" id="title" name="title">
            </div>
            <div class="form-group m-1">
              <label for="post">Post</label>
              <textarea class="form-control" type="text" id="post" name="post" rows="6"></textarea>
            </div>
            <div class="form-check">
              <input type="checkbox" id="likedGame" name="likedGame">
              <label class="checkbox-inline" for="likedGame">Liked the Game</label>
            </div>
            <div class="form-group">
              <button class="btn btn-primary mb-3" type="button" @click.prevent="postGameReview">Post</button>
            </div>
          </form>
        </div>
      </div>
    </div>

    <!-- List of game reviews -->
    <button type="button" class="btn btn-primary mb-3" @click="fetchGameReviews"> Fetch Game Reviews </button>
    
    <div v-for="review in game_reviews.slice().reverse()">

      <div class="card text-center mb-3" >

        <div class="card-body">
          <h5 class="card-title">{{ review.title }}</h5>
          <p class="card-text">{{ review.post }}</p>
          <span v-if="review.likedGame">I liked this game! &#128077;</span>
          <span v-else>I did not like this game! &#128078; </span>
          <p>Posted at {{ formatTime(review.dateTime) }}</p>
          <div class="row">

            <div class="col-sm-12 text-center m-2">
              <!-- <p id="game_review_id">{{ review.id }}</p> -->
              <button type="button" class="btn btn-primary m-1" @click="updateGameReview(review.id, true)">Liked the Game</button>
              <button type="button" class="btn btn-danger m-1" @click="updateGameReview(review.id, false)">Dislike the Game</button>
            </div>
            <div>
              <button class="btn btn-danger m-1" @click="deleteGameReview(review.id)">Delete Review</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import moment from 'moment';
  export default{
    data() {
      return{
        game_reviews: []

      }
    },
    methods: {
      
      // Perform an Ajax request to fetch list of the game reviews
      async fetchGameReviews(){
        let response = await fetch('http://localhost:8000/api/game_reviews/')
        let data = await response.json()
        this.game_reviews = data.game_reviews
        console.log(this.game_reviews)
        // alert("Game reviews fetched!")
      },
      
      // Perform an Ajax request to post a game review
      async postGameReview(){
        console.log(document.getElementById('likedGame').checked)

        let response = await fetch('http://localhost:8000/api/game_reviews/', {
          method: 'post',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            title: document.getElementById('title').value,
            post: document.getElementById('post').value,
            likedGame: document.getElementById('likedGame').checked,
            
          })
        })
        let data = await response.json()
        this.game_reviews = data.game_reviews

        alert('Game review posted!')
        let form = document.getElementsByName('gameReview-form')[0];
        form.reset();
        this.fetchGameReviews()

      },

      //Perform an Ajax request to update a rating of a game review
      async updateGameReview(id, value){
        
        let response = await fetch('http://localhost:8000/api/game_reviews/' + id +'/', {
          method: 'put',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            // id: document.getElementById('game_review_id').innerHTML,
            likedGame: value,
          })
        })
        let data = await response.json()
        this.game_reviews = data.game_reviews
        alert('Game review rating updated!')
        this.fetchGameReviews()
      },

      // Perform an Ajax request to delete a game review
      async deleteGameReview(id){
        let response = await fetch('http://localhost:8000/api/game_reviews/' + id +'/', {
          method: 'delete',
          headers: {
            'Content-Type': 'application/json',
          },
        })
        let data = await response.json()
        this.game_reviews = data.game_reviews
        alert('Game review deleted!')
        this.fetchGameReviews()
      },

      // // Method to show buttons
      // ShowButtons(){
      //   var x = document.getElementById("HideButtons");
      //   if (x.style.display === "none") {
      //     x.style.display = "block";
      //   } else {
      //     x.style.display = "none";
      //   }
      // },


      // Method for time formatting
      formatTime(value){
        return moment(value).format('MMMM Do YYYY, h:mm:ss a')
      },
      

      //Method for changing colour of background
      colourChange(value){
        if (value  == true){
          return 'bg-success'
        }
        else{
          return 'bg-danger'
        }
      }
    }
  }
</script>

<!-- <style>
.reverse{
  display: flex;
  flex-direction: column-reverse;
}
</style> -->

