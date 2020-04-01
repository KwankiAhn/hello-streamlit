import graphviz 

class  Digraph:
    def save_graph_as_svg(self, dot_string, output_file_name, file_format):
        if type(dot_string) is str:
            g = graphviz.Source(dot_string)
        elif isinstance(dot_string, (graphviz.dot.Digraph, graphviz.dot.Graph)):
            g = dot_string
        g.format=file_format
        g.filename = output_file_name
        g.directory = 'res/images/markdown_img/'
        g.render(view=False)
        return g, g.directory
    