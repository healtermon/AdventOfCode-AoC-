;; -*- lexical-binding: t; -*-

(defun get-lines-list (filename)
  "Give FILENAME, return data suitable for processing by
further functions."
  (with-temp-buffer
    (insert-file-contents filename)
    (let ((file-contents (buffer-string)))
      (string-lines (string-chop-newline file-contents)))))

(defun define-partition (str offset)
  "Divide string STR into groups of *NUM-DISTINCT-CHARS*, starting at OFFSET.

Return partitioned list with number of omitted characters,
OFFSET, consed to the front. This number is necessary for
computing the number of characters seen before we can identify a
start-of-packet marker."
  (let ((partition (seq-partition (substring str offset) *num-distinct-chars*)))
    (cons offset partition)))

(defun define-expansion (str)
  "Compute and return all *NUM-DISTINCT-CHARS* possible
partitionings with offset for STR."
  (mapcar (lambda (index)
            (define-partition str index))
          (number-sequence 0 (1- *num-distinct-chars*))))

(defun some-letters-repeat-p (str)
  "Helper predicate used to filter out letter groups with either
fewer than *NUM-DISTINCT-CHARS*, or else those that have
*NUM-DISTINCT-CHARS* characters but repeat at least one letter."
  (< (length (seq-uniq str)) *num-distinct-chars*))

(defun compute-partition-score (partition)
  "Compute and return, for PARTITION, the number of characters seen
before successful identification of a start-of-packet (or
start-of-message) marker."
  (seq-let (offset &rest members) partition
    (let ((truncated (seq-take-while #'some-letters-repeat-p members)))
      (+ offset
         (* *num-distinct-chars* (length truncated))
         *num-distinct-chars*))))


(defun first-marker (str)
  "Compute and return the number of characters corresponding to the
earliest appearance of a start-of-packet (or start-of-message)."
  (seq-min (mapcar #'compute-partition-score (define-expansion str))))

;; Tests, using the examples for the current day
(defvar *example1* "bvwbjplbgvbhsrlpgdmjqwftvncz"
  "First example in part 1.")
(defvar *example2*  "nppdvjthqldpwncqszvftbrmjlhg"
  "Second example in part 1.")
(defvar *example3* "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
  "Third example in part 1.")
(defvar *example4* "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
  "Fourth example in part 1.")
(defvar *example5* "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
  "First example in part 2, added to the front of the previous set of examples.
Here, I'm simply appending it.") ;; added in part 2

(defun test-aoc-part (part-1-p)
  "Test current solution based on examples given in the current
day's problem description.

With an argument of T, solve Part 1.
With an argument of NIL, solve Part 2."
  (require 'ert)
  (if part-1-p
      (progn
        (should (= 5 (first-marker *example1*)))
        (should (= 6 (first-marker *example2*)))
        (should (= 10 (first-marker *example3*)))
        (should (= 11 (first-marker *example4*))))

    ;; Test part 2 instead
    (should (= 23 (first-marker *example1*)))
    (should (= 23 (first-marker *example2*)))
    (should (= 29 (first-marker *example3*)))
    (should (= 26 (first-marker *example4*)))
    (should (= 19 (first-marker *example5*)))))

(defun test-part-problem-specific (part-1-p)
  "Run the tests defined in TEST-AOC-PART, but tailoring the
argument(s) based on wether Part 1 or Part 2 is selected."
  (defvar *num-distinct-chars*)
  (let ((*num-distinct-chars* (if part-1-p 4 14)))
    (test-aoc-part part-1-p)))

(defun solve (part-1-p)
  "Solve the specified part.

If PART-1-P is T, solve Part 1.
If PART-2-P is NIL, solve Part 2."
  (defvar *num-distinct-chars*)
  (let ((*num-distinct-chars* (if part-1-p 4 14))
        (input-string (car (get-lines-list "input.txt"))))
    (first-marker input-string)))

(defun solve-both-parts ()
  "The current day's \"main\" function.

Return a two element list consisting of Day 6's Part 1 and Part 2
answers."
  (test-part-problem-specific t)
  (test-part-problem-specific nil)

  ;; Part 1
  (list

   ;; 1896
   (solve t)

   ;; 3452
   (solve nil)))

(message "Solutions for Parts 1 and 2: %s" (solve-both-parts))
