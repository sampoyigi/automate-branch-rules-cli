"""Change the config values."""
branches = ('master',)  # Note: Single element requires a comma at end.
add_codeowners_file = False
signed_commit = False
branch_rules = {"required_approving_review_count": 1,
                "dismiss_stale_reviews": True,
                "user_push_restrictions": [],
                "team_push_restrictions": [],
                "contexts": [],
                "strict": True
                }
