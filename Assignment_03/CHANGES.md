# Assignment 03 — CHANGES

**Name:**   TOE TWEL TAR HTUT  **Student ID:** 6705140007

This is the written part of your submission. Explain **what you changed and why**, then record your **prompt log**. Keep before/after snippets to a line or two.

---

## 1 · What I changed

One row per change. Name the OOP concept and say how you checked the behaviour was unchanged.

| # | Code smell in the original | What I changed it to | OOP concept applied | How I verified behaviour was unchanged |

|---|---|---|---|---|
| 1 | Magic numbers such as `0.07`, `100`, `10`, and `0.03` were used directly in the code. | Replaced them with named constants such as `TAX_RATE`, `DISCOUNT_THRESHOLD`, and `BULK_DISCOUNT_RATE`. | Clean code / Named constants | Kept the original values unchanged and checked the final output with the self-test. |

| 2 | Products were stored as tuples containing name, price, and category. | Created a `Product` class with `name`, `price`, and `category` attributes. | Classes / Encapsulation | Checked that all original product values were preserved and the self-test passed. |

| 3 | Order items were stored as `(product_index, quantity)` tuples. | Created an `OrderItem` class containing a `Product` object and `quantity`, with quantity validation. | Composition / Encapsulation | Kept the original quantities and verified the final output with the self-test. |

| 4 | Membership tiers used repeated `if/elif` conditions for discounts and points. | Created `Customer`, `SilverCustomer`, `GoldCustomer`, and `PlatinumCustomer` classes with overridden methods. | Inheritance / Polymorphism | Kept the original discount rates and points multipliers and verified the self-test. |

| 5 | Customer name and membership tier were stored as tuple values. | Stored customer information in `Customer` objects using attributes such as `name` and `tier`. | Classes / Encapsulation | Checked that the receipt still displayed the same customer names and tiers. |

| 6 | The original `calc()` function handled calculations, receipt printing, and order data together. | Created an `Order` class with separate methods for `subtotal()`, `discount()`, `tax()`, `total()`, and `points()`. | Composition / Pure methods | Compared the refactored output with the original output using the self-test. |

| 7 | Calculation logic and receipt printing were mixed together. | Created a separate `receipt()` method for receipt output while calculation methods return values. | Separation of calculation and I/O | Verified that the final output remained identical and the self-test passed. |

| 8 | The original program used raw tuples and a procedural main function. | `refactored_main()` now creates and connects the OOP objects while preserving the original orders and output. | Refactoring / OOP design | Ran `python Assignment_03.py` and checked for `PASS`. |

## 2 · Short reflection (4–6 sentences)

Which change improved the code the most, and why? Where did keeping the behaviour identical force you to be careful?

> The Order class improved the code the most because it organized the order data and separated each calculation into its own method. Using customer subclasses also made the discount and points logic clearer by replacing repeated if/elif conditions with polymorphism. Keeping the behavior identical required me to be careful with the original discount thresholds, tax rates, points calculations, and receipt formatting. Even small changes to values, conditions, or printed text could cause the self-test to fail.

---

## 3 · Prompt log (Level 2 — required)

Record **every** prompt where AI helped. If you wrote a part yourself, say so in one row. AI-shaped code with an empty log does **not** meet the Level-2 policy.

| # | My prompt to the AI | What it suggested (summary) | Accept / reject / edited | How I checked it |
|---|---|---|---|---|

| 1 | Revisse through Assignment 03 step by step using the Week 2–5 lecture concepts. | Broke the refactoring task into classes, encapsulation, inheritance, polymorphism, composition, calculation methods, and receipt output. | Accepted | Compared the plan with the assignment requirements and Week 2–5 slides. |


| 2 | Show how to refactor the product and order-item tuples into proper OOP classes. | Suggested `Product` and `OrderItem` classes, including price and quantity validation and the Product relationship. | Accepted | Compared the new attributes and validation rules with the original data structures. |

| 3 | Replace the membership-tier `if/elif` logic with inheritance and polymorphism. | Suggested a `Customer` base class with `SilverCustomer`, `GoldCustomer`, and `PlatinumCustomer` subclasses using common methods. | Edited | Checked each discount rate and points multiplier against the original business rules. |

| 4 | Help me build the `Order` class while keeping the original calculations and output unchanged. | Suggested `Order` composition plus separate `subtotal()`, `discount()`, `tax()`, `total()`, `points()`, and `receipt()` methods. | Edited | Compared the formulas, thresholds, tax rules, and receipt format with the legacy code. |

| 5 | Provide the guided refactored section step by step, including `refactored_main()`, while comparing the original behaviour. | Combined the classes, calculations, receipt generation, and original products and orders into the refactored program. | Edited | Reviewed the code against the legacy section and planned final verification with the built-in self-test. |

**Ownership statement.** *By submitting, I confirm I understand and can explain every line of code I submitted, and that this prompt log reflects my actual AI use.*

---

## 4 · Before-you-submit checklist

- [ ] `python Assignment_03.py` prints **PASS**.
- [ ] No tuples / parallel lists left — products, orders, and items are objects.
- [ ] No `if tier == ...` chains — tiers are a class family.
- [ ] Calculation methods **return** values and do not `print`; printing is separate.
- [ ] Constructors validate state; no leftover `global`; magic numbers are named.
- [ ] The change table and reflection above are filled in.
- [ ] The prompt log is complete and the ownership statement is signed.
