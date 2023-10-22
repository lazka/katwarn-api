Things I noticed about the API:

* The "notifiable" field of an alert is returned as a string, but looks like it
  should be a boolean
* In some cases the incidents index lists incident IDs which can't be fetched
  (404)
