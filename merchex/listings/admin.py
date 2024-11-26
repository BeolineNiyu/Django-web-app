class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_publication', 'auteur')
    search_fields = ('titre', 'contenu')
    list_filter = ('date_publication', 'auteur')

    # Organiser les champs du formulaire
    fieldsets = (
        (None, {
            'fields': ('titre', 'contenu')
        }),
        ('Date et Auteur', {
            'fields': ('date_publication', 'auteur'),
            'classes': ('collapse',),  # Réduit cette section
        }),
    )

admin.site.register(Article, ArticleAdmin)

