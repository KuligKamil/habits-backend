# Type queries into this side of the screen, and you will 
# see intelligent typeaheads aware of the current GraphQL type schema, 
# live syntax, and validation errors highlighted within the text.

# We'll get you started with a simple query showing your username!
query {
  viewer {
    login
     repositories {
          totalCount
        }
    followers(first:10) {
      totalCount
      nodes {
        login
        avatarUrl
        repositories {
          totalCount
        }
        followers(first: 10) {
          totalCount
        }
      }
    } 
  }
}
# query { 
#   sinem: user( login: "brzezinskimarcin" ) {
#     repositories(first: 3, isFork: false, orderBy: {field: PUSHED_AT direction: DESC}) {
#       nodes {
#         name
#         url
#         updatedAt
#         defaultBranchRef {
#                 target {
#             ... on Commit {
#               history {
#                 totalCount
#               }
#             }
#           }
#         }
#       }
#     }
#   }
# }
# query {
#   repository(owner:"rails", name:"rails") {
#     defaultBranchRef {
#       target {
#         ... on Commit {
#           history {
#             totalCount
#           }
#         }
#       }
#     }
#   }
# }