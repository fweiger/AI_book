namespace PITNoLookahead

/-- A data observation distinguishes when the event happened from when
the strategy could first know the observation. -/
structure Observation (α : Type) where
  eventTime : Nat
  availableAt : Nat
  value : α
deriving Repr

/-- The eligibility filter is intentionally based on availableAt,
not eventTime. It returns all rows that could have been known at t. -/
def eligibleRows {α : Type} (decisionTime : Nat)
    (rows : List (Observation α)) : List (Observation α) :=
  rows.filter (fun row => decide (row.availableAt ≤ decisionTime))

/-- No row admitted by the point-in-time eligibility filter can have
become available after the decision time. -/
theorem eligibleRows_no_lookahead {α : Type} (decisionTime : Nat)
    (rows : List (Observation α)) :
    ∀ row ∈ eligibleRows decisionTime rows,
      row.availableAt ≤ decisionTime := by
  intro row hrow
  have hmem := List.mem_filter.mp hrow
  exact of_decide_eq_true hmem.2

/-- A late-arriving revision is excluded even when its underlying event
occurred before the strategy decision. -/
theorem late_available_revision_excluded {α : Type}
    (decisionTime : Nat) (row : Observation α)
    (hlate : decisionTime < row.availableAt) :
    row ∉ eligibleRows decisionTime [row] := by
  intro hmem
  have hsafe := eligibleRows_no_lookahead decisionTime [row] row hmem
  exact Nat.not_lt_of_ge hsafe hlate

/-- Example: the event happened at time 1, but the corrected value only
became available at time 3. A decision at time 2 must not see it. -/
def lateCorrection : Observation Nat :=
  { eventTime := 1, availableAt := 3, value := 42 }

theorem late_correction_event_precedes_decision :
    lateCorrection.eventTime ≤ 2 := by
  decide

theorem late_correction_not_available_at_decision :
    lateCorrection ∉ eligibleRows 2 [lateCorrection] := by
  apply late_available_revision_excluded
  decide

#print axioms eligibleRows_no_lookahead
#print axioms late_available_revision_excluded

end PITNoLookahead
